(this["webpackJsonpmy-gui"]=this["webpackJsonpmy-gui"]||[]).push([[0],{14:function(e,t,a){},223:function(e,t,a){"use strict";a.r(t);var n=a(0),r=a.n(n),s=a(35),c=a.n(s),i=(a(94),a(14),a(2)),o=a.n(i),u=a(3),l=a(5),m=a(6),p=a(7),h=a(8),d=a(9),f=a(84),v=a.n(f),b=(a(23),function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){return r.a.createElement("nav",null,r.a.createElement("a",{href:"/"},r.a.createElement("img",{style:{width:30,height:30},src:v.a})),r.a.createElement("ul",{className:"nav-links"},r.a.createElement(d.b,{className:"top_bar_links",to:"/about"},r.a.createElement("li",null,"About")),r.a.createElement(d.b,{className:"top_bar_links",to:"/users"},r.a.createElement("li",null,"Users"))))}}]),a}(n.Component));var g=function(){return r.a.createElement("div",null,r.a.createElement("h1",null,"About Page"))},E=(a(24),a(10)),O=a(15),w=a.n(O),j=a(87),y=a.n(j).a.create({baseURL:"/api"});function k(){return x.apply(this,arguments)}function x(){return(x=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users");case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function C(e){return S.apply(this,arguments)}function S(){return(S=Object(u.a)(o.a.mark((function e(t){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t));case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function _(e){return H.apply(this,arguments)}function H(){return(H=Object(u.a)(o.a.mark((function e(t){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t,"/feelings"));case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function I(e){return N.apply(this,arguments)}function N(){return(N=Object(u.a)(o.a.mark((function e(t){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t,"/snapshots"));case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function D(e,t){return M.apply(this,arguments)}function M(){return(M=Object(u.a)(o.a.mark((function e(t,a){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t,"/snapshots/").concat(a));case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function P(e,t,a){return z.apply(this,arguments)}function z(){return(z=Object(u.a)(o.a.mark((function e(t,a,n){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t,"/snapshots/").concat(a,"/").concat(n));case 2:return e.abrupt("return",e.sent.data);case 3:case"end":return e.stop()}}),e)})))).apply(this,arguments)}function A(e,t,a){return R.apply(this,arguments)}function R(){return(R=Object(u.a)(o.a.mark((function e(t,a,n){var r;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,y.get("/users/".concat(t,"/snapshots/").concat(a,"/").concat(n,"/data"));case 2:return r=e.sent,r.data,e.abrupt("return",r.data);case 5:case"end":return e.stop()}}),e)})))).apply(this,arguments)}var W=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return n.props.match,console.log(k()),e.next=4,k();case 4:t=e.sent,n.setState({items:t});case 6:case"end":return e.stop()}}),e)}))),n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state.items,t=(this.props.match,[{Header:"User Id",accessor:"user_id",Cell:function(e){return r.a.createElement("a",{className:"navStyle",onClick:"handleClick",href:"/users/".concat(e.original.user_id)},e.original.user_id)}},{Header:"User Name",accessor:"user_name"}]);return r.a.createElement("div",{className:"table-header animated fadeInLeft"},r.a.createElement("h1",{className:"titles"},"Users"),r.a.createElement(E.a,{data:e,columns:t,defaultPageSize:5,minRows:0}))}}]),a}(n.Component),U=a(20),T=a.n(U),B=a(27),L=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).state={chartData:e.chartData},n}return Object(m.a)(a,[{key:"render",value:function(){return console.log(this.props.chartData),r.a.createElement("div",null,r.a.createElement("div",{className:"bchart"},r.a.createElement(B.a,{data:this.props.chartData,height:450,width:600,options:{title:{display:"",text:"Feelings",fontSize:25},legend:{display:this.props.displayLegend,position:"right"},responsive:!0,maintainAspectRatio:!1}})),r.a.createElement("div",{className:"pchart"},r.a.createElement(B.c,{data:this.props.chartData,height:400,width:500,options:{responsive:!1,maintainAspectRatio:!1}})))}}]),a}(n.Component);L.defaultProps={displayTitle:!0,displayLegend:!1,legendPosition:"right",location:"City"};var X=L,Y=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).state={chartData:e.chartData},n}return Object(m.a)(a,[{key:"render",value:function(){return console.log(this.props.chartData),r.a.createElement("div",null,r.a.createElement(B.b,{data:this.props.chartData,height:450,width:600,options:{title:{display:"{true}}",text:"Feelings over time",fontSize:25},legend:{display:this.props.displayLegend,position:"top"},scales:{xAxes:[{type:"time",time:{unit:"minute"}}]},responsive:!1,maintainAspectRatio:!0}}))}}]),a}(n.Component);Y.defaultProps={displayTitle:!0,displayLegend:!0,legendPosition:"top",location:"City"};var F=Y,J=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a,r,s,c,i,u,l,m;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,C(t.params.id);case 3:return a=e.sent,e.next=6,_(t.params.id);case 6:r=e.sent,n.setState({user:a}),console.log(a),s=Object.keys(r).map((function(e){return r[e].feelings_at_timestamp.exhaustion})),c=Object.keys(r).map((function(e){return r[e].feelings_at_timestamp.happiness})),i=Object.keys(r).map((function(e){return r[e].feelings_at_timestamp.hunger})),u=Object.keys(r).map((function(e){return r[e].feelings_at_timestamp.thirst})),l=Object.keys(r).map((function(e){return r[e].timestamp})),m={labels:l,datasets:[{label:"Hunger",data:i,backgroundColor:["rgba(75, 192, 192, 0.6)"],borderWidth:1,pointRadius:0},{label:"Exhaustion",data:s,backgroundColor:["rgba(255, 99, 132, 0.6)"],borderWidth:1,pointRadius:0},{label:"Happiness",data:c,backgroundColor:["rgba(255, 206, 86, 0.6)"],borderWidth:1,pointRadius:0},{label:"Thirst",data:u,backgroundColor:["rgba(255, 159, 64, 0.6)"],borderWidth:1,pointRadius:0}]},n.setState({exhaustion:m});case 16:case"end":return e.stop()}}),e)}))),n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.props.match,t=[{Header:"User Id",accessor:"user_id"},{Header:"User Name",accessor:"user_name"},{Header:"User Birthday",Cell:function(e){return r.a.createElement("td",null,r.a.createElement(T.a,{format:"MMMM Do YYYY",unix:!0},e.original.birthday))}},{Header:"User Gender",accessor:"gender"},{Header:"snapshots",Cell:function(t){return r.a.createElement("a",{className:"navStyle",href:"/users/".concat(e.params.id,"/snapshots/")},"View Snapshots")}}];return r.a.createElement("div",{className:"table-header "},r.a.createElement("h1",{className:"titles"},"User Details"),r.a.createElement(E.a,{data:this.state.user,columns:t,defaultPageSize:5,minRows:0,showPagination:!1}),r.a.createElement("div",{className:"feelings-over-time"},r.a.createElement(F,{chartData:this.state.exhaustion})))}}]),a}(n.Component),Z=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,I(t.params.id);case 3:a=e.sent,n.setState({items:a});case 5:case"end":return e.stop()}}),e)}))),n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state.items,t=this.props.match,a=[{Header:"Snapshot Id",accessor:"snapshot_id",Cell:function(e){return r.a.createElement("a",{className:"navStyle",href:"/users/".concat(t.params.id,"/snapshots/").concat(e.original.snapshot_id)},e.original.snapshot_id)}},{Header:"Snapshot Date-Time",accessor:"datetime",Cell:function(e){return r.a.createElement("td",null,r.a.createElement(T.a,{format:"MMMM Do, h:mm:ss a",unix:!0},e.original.datetime))}}];return r.a.createElement("div",null,r.a.createElement("h1",{className:"page-header table-header animated fadeInLeft titles "},"Snapshots"),r.a.createElement(E.a,{className:"ReactTable animated fadeInLeft ",showPageSizeOptions:!0,pageSizeOptions:[10,20,50,100],defaultPageSize:10,defaultSortDesc:!0,defaultSorted:[{id:"datetime",desc:!1}],defaultResized:[23],data:e,columns:a}))}}]),a}(n.Component),G=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,D(t.params.id,t.params.snapshot);case 3:a=e.sent,n.setState({items:a});case 5:case"end":return e.stop()}}),e)}))),n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state.items,t=this.props.match;if(console.log({items:e}),!e)return null;var a=[{Header:"Snapshot Id",accessor:"snapshot_id"},{Header:"Snapshot Date-Time",Cell:function(e){return r.a.createElement("td",null,r.a.createElement(T.a,{format:"MMMM Do, h:mm:ss a",unix:!0},e.original.date_time))}},{Header:"Available Results",accessor:"available_results",Cell:function(e){return r.a.createElement("div",{className:"array"},e.original.available_results.map((function(e){return r.a.createElement(d.b,{className:"navStyle",to:"/users/".concat(t.params.id,"/snapshots/").concat(t.params.snapshot,"/").concat(e)},e)})))}}];return r.a.createElement("div",{className:"table-header"},r.a.createElement("h2",{className:"titles"},"Snapshot Details"),r.a.createElement(E.a,{data:e,columns:a,defaultPageSize:1,showPagination:!1}))}}]),a}(n.Component),V=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(){var e;return Object(l.a)(this,a),(e=t.call(this)).componentWillMount=Object(u.a)(o.a.mark((function t(){return o.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.fetchItems();case 2:case"end":return t.stop()}}),t)}))),e.fetchItems=Object(u.a)(o.a.mark((function t(){var a,n,r;return o.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return a=e.props.match,t.next=3,P(a.params.id,a.params.snapshot,"feelings");case 3:n=t.sent,Object.keys(n[0]),r={labels:["Exhaustion","Happiness","Hunger","Thirst"],datasets:[{label:"",data:Object.values(n[0]),backgroundColor:["rgba(255, 99, 132, 0.6)","rgba(54, 162, 235, 0.6)","rgba(255, 206, 86, 0.6)","rgba(75, 192, 192, 0.6)","rgba(153, 102, 255, 0.6)","rgba(255, 159, 64, 0.6)","rgba(255, 99, 132, 0.6)"]}]},e.setState({chartData:r});case 7:case"end":return t.stop()}}),t)}))),e.state={chartData:[]},e}return Object(m.a)(a,[{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement("h1",{className:"titles"},"Feelings"),r.a.createElement(X,{chartData:this.state.chartData}))}}]),a}(n.Component),$=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a,r;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,P(t.params.id,t.params.snapshot,"color_image");case 3:return a=e.sent,e.next=6,A(t.params.id,t.params.snapshot,"color_image");case 6:r=e.sent,n.setState({items:a}),n.setState({image_src:r});case 9:case"end":return e.stop()}}),e)}))),n.onButtonClickHandler=function(e){return function(t){window.alert(e)}},n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:return e.next=4,this.fetchData();case 4:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=(this.props.match,this.state.items),a=this.state.image_src;if(!t)return null;var n=[{Header:"Image Width",accessor:"width"},{Header:"Image Height",accessor:"height"},{Header:"Image Path",accessor:"parsed_path",Cell:function(t){return r.a.createElement("div",{className:"navStyle"},r.a.createElement("button",{onClick:e.onButtonClickHandler(t.original.parsed_path)},"view file path"))}}];return r.a.createElement("div",{className:"table-header"},r.a.createElement("h1",{className:"titles"},"Color Image"),r.a.createElement(E.a,{showPagination:!1,data:t,columns:n,defaultPageSize:1}),r.a.createElement("view",null,r.a.createElement("img",{className:"animated fadeIn color-image",src:a,resizeMode:"contain",style:{maxHeight:480,maxWidth:640}})))}}]),a}(n.Component),q=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a,r;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,P(t.params.id,t.params.snapshot,"depth_image");case 3:return a=e.sent,e.next=6,A(t.params.id,t.params.snapshot,"depth_image");case 6:r=e.sent,n.setState({items:a}),n.setState({image_src:r});case 9:case"end":return e.stop()}}),e)}))),n.onButtonClickHandler=function(e){return function(t){window.alert(e)}},n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.fetchItems();case 2:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=(this.props.match,this.state.items),a=this.state.image_src;if(!t)return null;var n=[{Header:"Image Width",accessor:"width"},{Header:"Image Height",accessor:"height"},{Header:"Image Path",accessor:"parsed_path",Cell:function(t){return r.a.createElement("div",{className:"navStyle"},r.a.createElement("button",{onClick:e.onButtonClickHandler(t.original.parsed_path)},"view file path"))}}];return r.a.createElement("div",{className:"table-header"},r.a.createElement("h1",{className:"titles"},"depth Image"),r.a.createElement(E.a,{showPagination:!1,data:t,columns:n,defaultPageSize:1}),r.a.createElement("view",null,r.a.createElement("img",{className:"animated fadeIn color-image",src:a,resizeMode:"contain",style:{maxHeight:480,maxWidth:640}})))}}]),a}(n.Component),K=function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).fetchItems=Object(u.a)(o.a.mark((function e(){var t,a;return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=n.props.match,e.next=3,P(t.params.id,t.params.snapshot,"pose");case 3:a=e.sent,n.setState({items:a}),console.log({items:a});case 6:case"end":return e.stop()}}),e)}))),n.onButtonClickHandler=function(e){return function(t){window.alert(e)}},n.state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(u.a)(o.a.mark((function e(){return o.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return this.props.match,e.next=3,this.fetchItems();case 3:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state.items;this.props.match;if(!e)return null;return r.a.createElement("div",{className:"table-header"},r.a.createElement("h2",{className:"titles"},"User Position"),r.a.createElement("h5",null,"Translation"),r.a.createElement(E.a,{showPagination:!1,data:e,columns:[{Header:"X",accessor:"translation[0]"},{Header:"Y",accessor:"translation[1]"},{Header:"Z",accessor:"translation[2]"}],defaultPageSize:1}),r.a.createElement("h5",null,"Rotation"),r.a.createElement(E.a,{showPagination:!1,data:e,columns:[{Header:"X",accessor:"rotation[0]"},{Header:"Y",accessor:"rotation[1]"},{Header:"Z",accessor:"rotation[2]"},{Header:"W",accessor:"rotation[3]"}],defaultPageSize:1}))}}]),a}(n.Component),Q=(a(77),a(206),a(11)),ee=(Object(Q.a)(),function(e){Object(h.a)(a,e);var t=Object(p.a)(a);function a(e){var n;return Object(l.a)(this,a),(n=t.call(this,e)).state={},n}return Object(m.a)(a,[{key:"componentDidMount",value:function(){w()("button").on("click",(function(){w()(this).addClass("animated flipOutX").one("animationend oAnimationEnd mozAnimationEnd webkitAnimationEnd",(function(){w()(this).removeClass("animated flipOutX")})),setTimeout((function(){document.location.href="/users"}),770)}))}},{key:"handleHover",value:function(){w()("button").on("click",(function(){w()(this).addClass("animated flipOutX").one("animationend oAnimationEnd mozAnimationEnd webkitAnimationEnd",(function(){w()(this).removeClass("animated flipOutX")}))}))}},{key:"render",value:function(){return r.a.createElement("div",null,r.a.createElement("h1",{className:"welcome animated fadeIn"},"Welcome"),r.a.createElement("button",{className:"button-style animated tada"},"Start"))}}]),a}(n.Component)),te=a(18);var ae=function(){return r.a.createElement(d.a,null,r.a.createElement("div",{className:"App"},r.a.createElement(b,null),r.a.createElement(te.c,null,r.a.createElement(te.a,{path:"/",exact:!0,component:ee}),r.a.createElement(te.a,{path:"/about",component:g}),r.a.createElement(te.a,{path:"/users",exact:!0,component:W}),r.a.createElement(te.a,{path:"/users/:id",exact:!0,component:J}),r.a.createElement(te.a,{path:"/users/:id/snapshots",exact:!0,component:Z}),r.a.createElement(te.a,{path:"/users/:id/snapshots/:snapshot",exact:!0,component:G}),r.a.createElement(te.a,{path:"/users/:id/snapshots/:snapshot/feelings",component:V}),r.a.createElement(te.a,{path:"/users/:id/snapshots/:snapshot/pose",component:K}),r.a.createElement(te.a,{path:"/users/:id/snapshots/:snapshot/color_image",exact:!0,component:$}),r.a.createElement(te.a,{path:"/users/:id/snapshots/:snapshot/depth_image",exact:!0,component:q}))))};Boolean("localhost"===window.location.hostname||"[::1]"===window.location.hostname||window.location.hostname.match(/^127(?:\.(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)){3}$/));c.a.render(r.a.createElement(r.a.StrictMode,null,r.a.createElement(ae,null)),document.getElementById("root")),"serviceWorker"in navigator&&navigator.serviceWorker.ready.then((function(e){e.unregister()})).catch((function(e){console.error(e.message)}))},23:function(e,t,a){},77:function(e,t,a){},84:function(e,t,a){e.exports=a.p+"static/media/home_icon.7acc70e6.png"},89:function(e,t,a){e.exports=a(223)},94:function(e,t,a){}},[[89,1,2]]]);
//# sourceMappingURL=main.34e09a8b.chunk.js.map