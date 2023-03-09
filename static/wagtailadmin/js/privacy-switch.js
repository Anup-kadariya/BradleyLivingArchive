(()=>{"use strict";var e,t={83622:function(e,t,r){var o=this&&this.__importDefault||function(e){return e&&e.__esModule?e:{default:e}};t.__esModule=!0;var i=o(r(73609));i.default((function(){i.default("button.action-set-privacy").on("click",(function(){return ModalWorkflow({url:this.getAttribute("data-url"),onload:{set_privacy:function(e){i.default("form",e.body).on("submit",(function(){return e.postForm(this.action,i.default(this).serialize()),!1}));var t=i.default("input[name='restriction_type'][value='password']",e.body),r=i.default("input[name='restriction_type'][value='groups']",e.body),o=i.default(".password-field",e.body),a=i.default("#groups-fields",e.body);function n(){t.is(":checked")?(o.show(),a.hide()):r.is(":checked")?(o.hide(),a.show()):(o.hide(),a.hide())}n(),i.default("input[name='restriction_type']",e.body).on("change",n)},set_privacy_done:function(e,t){e.respond("setPermission",t.is_public),e.close()}},responses:{setPermission:function(e){e?(i.default(".privacy-indicator").removeClass("private").addClass("public"),i.default(".privacy-indicator-tag").addClass("u-hidden").attr("aria-hidden","true")):(i.default(".privacy-indicator").removeClass("public").addClass("private"),i.default(".privacy-indicator-tag").removeClass("u-hidden").attr("aria-hidden","false"))}}}),!1}))}))},73609:e=>{e.exports=jQuery}},r={};function o(e){var i=r[e];if(void 0!==i)return i.exports;var a=r[e]={id:e,loaded:!1,exports:{}};return t[e].call(a.exports,a,a.exports,o),a.loaded=!0,a.exports}o.m=t,e=[],o.O=(t,r,i,a)=>{if(!r){var n=1/0;for(l=0;l<e.length;l++){for(var[r,i,a]=e[l],d=!0,s=0;s<r.length;s++)(!1&a||n>=a)&&Object.keys(o.O).every((e=>o.O[e](r[s])))?r.splice(s--,1):(d=!1,a<n&&(n=a));d&&(e.splice(l--,1),t=i())}return t}a=a||0;for(var l=e.length;l>0&&e[l-1][2]>a;l--)e[l]=e[l-1];e[l]=[r,i,a]},o.n=e=>{var t=e&&e.__esModule?()=>e.default:()=>e;return o.d(t,{a:t}),t},o.d=(e,t)=>{for(var r in t)o.o(t,r)&&!o.o(e,r)&&Object.defineProperty(e,r,{enumerable:!0,get:t[r]})},o.g=function(){if("object"==typeof globalThis)return globalThis;try{return this||new Function("return this")()}catch(e){if("object"==typeof window)return window}}(),o.hmd=e=>((e=Object.create(e)).children||(e.children=[]),Object.defineProperty(e,"exports",{enumerable:!0,set:()=>{throw new Error("ES Modules may not assign module.exports or exports.*, Use ESM export syntax, instead: "+e.id)}}),e),o.o=(e,t)=>Object.prototype.hasOwnProperty.call(e,t),o.r=e=>{"undefined"!=typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(e,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(e,"__esModule",{value:!0})},o.j=598,(()=>{var e={598:0};o.O.j=t=>0===e[t];var t=(t,r)=>{var i,a,[n,d,s]=r,l=0;for(i in d)o.o(d,i)&&(o.m[i]=d[i]);if(s)var u=s(o);for(t&&t(r);l<n.length;l++)a=n[l],o.o(e,a)&&e[a]&&e[a][0](),e[n[l]]=0;return o.O(u)},r=globalThis.webpackChunkwagtail=globalThis.webpackChunkwagtail||[];r.forEach(t.bind(null,0)),r.push=t.bind(null,r.push.bind(r))})(),o.O(void 0,[751],(()=>o(83622)));var i=o.O(void 0,[751],(()=>o(90971)));i=o.O(i)})();
//# sourceMappingURL=privacy-switch.js.map