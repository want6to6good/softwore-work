<template>
	<div id="login">
		<el-container>
			<el-header>
				<h1 style="color: #FFFFFF;margin-top: 25px;">在线招聘系统</h1>
			</el-header>
			<el-main>
				<div id="login-from">
					<el-form ref="loginForm" status-icon :model="loginForm" :rules="rules">
						<el-form-item label="用户名/邮箱/手机号" prop="username">
							<el-input v-model="loginForm.username" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<el-form-item label="密码" prop="password">
							<el-input type="password" v-model="loginForm.password" autocomplete="off"></el-input>
							</el-input>
						</el-form-item>
						<slide-verification @check-result="checkResult"></slide-verification>
						<br />
						<el-button type="primary" @click.native.prevent="handLogin('loginForm')">登录</el-button>
						<div class="text-foot">
							还没有账号?
							<router-link to="/register" class="register-link">
								注册
							</router-link>
						</div>
					</el-form>
				</div>
			</el-main>
		</el-container>
	</div>
</template>

<script>
	import SlideVerification from '@/components/SlideVerification.vue'
	export default {
		data() {
			return {
				confirmSuccess: false,
				loginForm: {
					username: null,
					password: null,
				},
				rules: {
					username: [{
						required: true,
						message: '请输入学号',
						trigger: 'blur'
					}],
					password: [{
						required: true,
						message: '请输入密码',
						trigger: 'blur'
					}]
				}
			}
		},
		components:{
			SlideVerification
		},
		methods: {
			//获取滑块验证结果
			checkResult(message) {
				this.confirmSuccess = message
			},
			//处理登录
			handLogin(formName) {
				//清理缓存信息
				localStorage.clear()
				sessionStorage.clear()
				if (this.confirmSuccess) {
					const msg = this
					this.$refs[formName].validate((valide) => {
						if (valide) {
							axios.post(`api/jwt-auth/`, this.loginForm).then(res => {
								console.log(res); //处理成功的函数 相当于success
								if (res.status == 200) {
									this.$message({
										message: '登录成功',
										type: 'success'
									});
									this.$store.commit("setUser", res.data.user)
									this.$store.commit("setStudent", res.data.student)
									this.$store.commit("setAuthorization", res.data.token)
									this.$router.push('/exam')
								}
							}).catch(function(error) {
								//错误处理 相当于error
								msg.$message('登录失败，账号或密码错误');
								console.log(error) 
							});
						} else {
							//表单验证失败
						}
					});
				} else {
					//未通过验证
					this.$message('请拖动滑块进行验证！');
				}
			}
		}
	}
</script>

<style lang="scss" scoped>
    #login {
        height: 100vh; // 使用视窗高度确保填满整个屏幕
        display: flex;
        align-items: center; // 垂直居中
        justify-content: center; // 水平居中
        background-image: url(../assets/bg.jpg);
        background-repeat: no-repeat;
        background-size: cover; 
        background-position: center; // 确保背景图片也居中
    }
	
    #login-from {
        width: 400px;
        height: 400px;
        border-radius: 10px;
        margin: auto; // 设置上下为自动，左右自动计算以居中
        display: flex; // 使用 flex 布局
        flex-direction: column; // 子元素垂直排列
        justify-content: center; // 子元素水平居中
        align-items: center; // 子元素垂直居中
        background-color: #FFFFFF;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); // 添加阴影效果增加立体感
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 20px;
    }

    .el-form {

		padding-top: 20px;
		margin: 50px 50px;
		width: 300px;

    }

    .el-input {
        width: 100%; // 使输入框和按钮宽度一致且填满其容器
    }

    .el-button {
        margin-top: 20px; // 为按钮添加上边距
        height: 40px; // 设置按钮高度
        background-color: #409EFF; // 设置按钮颜色
        color: white;
        border: none;
        border-radius: 5px; // 轻微圆角
        cursor: pointer;
        &:hover {
            background-color: darken(#409EFF, 10%); // 鼠标悬停时加深颜色
        }
    }

    .text-foot {
        margin-top: 20px;
        font-weight: 700;
        font-size: 14px; // 设置适当的文字大小
    }
</style>