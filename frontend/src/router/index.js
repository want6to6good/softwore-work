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
            path: 'list',
            name: 'JobList',
            component: () => import('../views/Job/JobList.vue'),
            meta: {
              title: '职位列表'
            }
          },
          {
            path: 'details/:id',
            name: 'JobDetails',
            component: () => import('../views/Job/JobDetails.vue'),
            meta: {
              title: '职位详情'
            }
          },
          {
            path: 'apply',
            name: 'JobApply',
            component: () => import('../views/Job/JobApply.vue'),
            meta: {
              title: '申请职位'
            }
          }
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
			}
		]
	},
// 	{
// 		path: '/',
// 		component: Layout,
// 		redirect: '/exam',
// 		children: [{
// 				path: 'exam',
// 				component: () => import('../views/Exam.vue'),
// 				name: 'exam',
// 				meta: {
// 					title: '考试中心'
// 				}
// 			},
// 			{
// 				path: 'practice',
// 				name: 'Practice',
// 				component: () => import('../views/Practice.vue'),
// 				meta: {
// 					title: '模拟练习'
// 				}
// 			},
// 			{
// 				path: 'grade',
// 				name: 'Grade',
// 				component: () => import('../views/Grade.vue'),
// 				meta: {
// 					title: '查询成绩'
// 				}
// 			},
// 			{
// 				path: 'center',
// 				name: 'Center',
// 				component: () => import('../views/Center.vue'),
// 				meta: {
// 					title: '个人中心'
// 				}
// 			},
// 			{
// 				path: 'password',
// 				name: 'Password',
// 				component: () => import('../views/Password.vue'),
// 				meta: {
// 					title: '修改密码'
// 				}
// 			},
// 			{
// 				path: 'paper',
// 				name: 'Paper',
// 				component: () => import('../views/Paper.vue'),
// 				meta: {
// 					title: '试卷详情'
// 				}
// 			},
// 			{
// 				path: 'score',
// 				name: 'Score',
// 				component: () => import('../views/Score.vue'),
// 				meta: {
// 					title: '考试得分'
// 				}
// 			}
// 		]
// },
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
		path: '/Pay',
		name: 'Pay',
		component: () => import('../views/Pay.vue'),
		meta: {
			title: '支付'
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
