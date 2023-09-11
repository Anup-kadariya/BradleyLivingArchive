from django.urls import reverse
from wagtail import hooks
from wagtail.admin.menu import MenuItem
from wagtail.models import PageViewRestriction
from wagtail.wagtail_hooks import require_wagtail_login

from blog.models import BlogDetailPage


@hooks.register("before_serve_page", order=-1)
def check_view_restrictions(page, request, *args, **kwargs):
    """
    Check whether there are any view restrictions on this page which are
    not fulfilled by the given request object. If there are, return an
    HttpResponse that will notify the user of that restriction (and possibly
    include a password / login form that will allow them to proceed). If
    there are no such restrictions, return None
    """
    if not isinstance(page, BlogDetailPage):
        return
    for restriction in page.get_view_restrictions():
        if not restriction.accept_request(request):
            if restriction.restriction_type == PageViewRestriction.PASSWORD:
                from wagtail.forms import PasswordViewRestrictionForm

                form = PasswordViewRestrictionForm(
                    instance=restriction,
                    initial={"return_url": request.get_full_path()},
                )
                action_url = reverse(
                    "wagtailcore_authenticate_with_password",
                    args=[restriction.id, page.id],
                )
                return page.serve_password_required_response(request, form, action_url)

            elif restriction.restriction_type == PageViewRestriction.LOGIN:
                return require_wagtail_login(next=request.get_full_path())
            elif restriction.restriction_type == PageViewRestriction.GROUPS:
                accept = True
                if not request.user.is_authenticated:
                    return require_wagtail_login(next=request.get_full_path())
                if not request.user.is_superuser:
                    current_user_groups = request.user.groups.all()

                    if not any(
                        group in current_user_groups
                        for group in restriction.groups.all()
                    ):
                        accept = False
                kwargs["accept"] = accept
                return page.serve(request, *args, **kwargs)
    return page.serve(request, *args, **kwargs)


@hooks.register("register_admin_menu_item")
def register_group_menu_item():
    return MenuItem(
        "My Groups", reverse("group_list"), classnames="icon icon-group", order=10000
    )


@hooks.register("construct_main_menu")
def add_user_group_management_menu_item(request, menu_items):
    user = request.user
    if not user.is_superuser:
        if not user.groups.filter(name="contributor").exists():
            menu_items[:] = [item for item in menu_items if item.name != "settings"]


# @hooks.register("construct_explorer_page_queryset")
# def show_own_pages_only(parent_page, pages, request):
#     user = request.user
#     # superuser
#     if user.is_superuser:
#         return pages
#
#     return pages.filter(owner=request.user)
