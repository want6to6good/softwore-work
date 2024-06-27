import Vue from 'vue'
import VueRouter from 'vue-router'
import Layout from '@/layout/index.vue'

Vue.use(VueRouter)

const routes = [
	  {
    path: '/job',
    component: Layout,
    children: [
		{
			path: '',
			component: () => import('../views/Job/JobMain.vue'),
			name: 'JobMain',
			meta: {
				title: '职位中心'
			}
		},
		{
			path: 'password',
			name: 'Password',
			component: () => import('../views/Job/Password.vue'),
			meta: {
				title: '修改密码'
			}
		},
		]
	},
{
  path: '/resume',
  component: Layout,
  children: [
	  {
		  path: '',
		  component: () => import('../views/Resume/ResumeMain.vue'),
		  name: 'ResumeMain',
		  meta: {
			  title: '简历中心'
		  }
	  },
        {
          path: 'view',
          name: 'ResumeView',
          component: () => import('../views/Resume/ResumeView.vue'),
          meta: {
            title: '查看简历'
          }
        }
  ]
},
	{
		path: '/message',
		component: Layout,
		children: [
			{
				path: '',
				component: () => import('../views/Message/MessageMain.vue'),
				name: 'MessageMain',
				meta: {
					title: '消息'
				}
			}
		]
	},
	{
		path: '/interview',
		component: Layout,
		children: [
		{
			path: '',
			component: () => import('../views/Interview/InterviewMain.vue'),
			name: 'InterviewMain',
			meta: {
			title: '模拟面试'
			}
		},
		{
			path: 'python',
			component: () => import('../views/Interview/Python.vue'),
			name: 'Python',
			meta: {
			title: 'Python 面试'
			}
		},
		{
			path: 'cpp',
			component: () => import('../views/Interview/Cpp.vue'),
			name: 'Cpp',
			meta: {
			title: 'C/C++ 面试'
			}
		},
		{
			path: 'vue3',
			component: () => import('../views/Interview/Vue3.vue'),
			name: 'Vue3',
			meta: {
			title: 'Vue3 面试'
			}
		},
		{
			path: 'java',
			component: () => import('../views/Interview/Java.vue'),
			name: 'Java',
			meta: {
			title: 'Java 面试'
			}
		},
		{
			path: 'javascript',
			component: () => import('../views/Interview/JavaScript.vue'),
			name: 'JavaScript',
			meta: {
			title: 'JavaScript 面试'
			}
		},
		{
			path: 'ruby',
			component: () => import('../views/Interview/Ruby.vue'),
			name: 'Ruby',
			meta: {
			title: 'Ruby 面试'
			}
			},
		{
		path: 'question/:id',
		component: () => import('../views/Interview/QuestionDetail.vue'),
		name: 'QuestionDetail',
		meta: {
			title: '题目详情'
		}
		}
		]
	},
	{
		path: '/answer',
		name: 'Answer',
		component: () => import('../views/Answer.vue'),
		meta: {
			title: '答题界面'
		}
	},
	{
		path: '/record',
		name: 'Record',
		component: () => import('../views/Record.vue'),
		meta: {
			title: '练习记录'
		}
	},
	{
		path: '/login',
		name: 'Login',
		component: () => import('../views/Login.vue'),
		meta: {
			title: '登录界面'
		}
	},
	{
		path: '/register',
		name: 'Register',
		component: () => import('../views/Register.vue'),
		meta: {
			title: '注册界面'
		}
	},
	{
		path: '*',
		name: 'Error',
		component: () => import('../views/Error.vue'),
		meta: {
			title: '404错误界面'
		}
	}
]

const router = new VueRouter({
	mode: 'history',
	base: process.env.BASE_URL,
	routes
})

// 导航守卫
// 使用 router.beforeEach 注册一个全局前置守卫，判断用户是否登陆
router.beforeEach((to, from, next) => {
	// 设置标题
	if (to.meta.title) {
		document.title = to.meta.title
	}

	if (to.path === '/login' || to.path === '/register') {
		next();
	} else {
		let token = sessionStorage.getItem('Authorization');
		if (token === null || token === '') {
			next('/login');
		} else {
			next();
		}
	}
});
export default router
