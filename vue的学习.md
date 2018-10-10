

'<div><p>{{title}}</p><button v-on:click="$emit(\'text\')">Enlarge text</button></div>'张种写法

# 普通的使用:
	- 先安装号node.js,后运行nmp init 后再运行nmp install vue安装vue



# 使用vue的脚手架: 
		- 首先再使用vue-cli之前需要下载nodejs,保证版本在4.4.5以上，然后运行npm install -g vue-cli,然后使用vue查看是否安装成功，使用
		  vue list 来查看你可以使用那些模板 
		  vue init webpack(使用那个模板) 项目名
		  运行后? Project name sell
			? Project description  sell app
			? Author zheng
			? Vue build standalone
			? Install vue-router? Yes
			? Use ESLint to lint your code? Yes
			? Pick an ESLint preset Standard
			? Set up unit tests No
			? Setup e2e tests with Nightwatch? No
			? Should we run `npm install` for you after the project has been created? (recommended) npm
	
# vue-router使用router.go('')来确定初始路由

# vue框架: 
	- elementui,iview,bootstrap,mintui


# 解决: 
	- 解决vue在页面加载是的闪烁为题， 加上v-cloak 再给这属性添加样式[v-cloak]:display:none
	在mounted里要对最新的dom操作的话需要加上$nextTick(()=>{})在里面进行dom的操作


# ES6语法：
	- ``: 为字符串模板，里面需要加参数是使用${}，例如`<li>${value}</li>`
	- 对数组的操作(主要写map,filter): filter: 表示从数组中过滤满足条件的子项组成数组，当返回为true是为新数组添加该项。
									```
										 例子：let arr = [1,2,3,4,5];
										 let arr2 = arr.filter(function (item) {
											return item>2&&item<5;
										 });
									 map: 表示为数组的每一项运行运行一个方法，方法的返回值就是数值的每一项
										例子: let arr3 = arr.map(value => {
												return `<li>${value}</li>`
											});
									```