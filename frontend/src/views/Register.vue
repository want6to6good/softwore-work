<template>
	<div id="register">
		<el-container>
			<el-header>
				<h1 style="color: #FFFFFF;margin-top: 25px;">在线招聘系统</h1>
			</el-header>
			<el-main>
				<div id="register-from">
					<el-form ref="registerForm" status-icon :model="registerForm" :rules="rules">
                        <el-form-item label="角色选择" prop="role">
                            <el-radio-group v-model="registerForm.role">
                                <el-radio label="hr">我是HR</el-radio>
                                <el-radio label="jobseeker">我是求职者</el-radio>
                            </el-radio-group>
                        </el-form-item>
                        <el-form-item label="公司名称" prop="company" required v-if="registerForm.role === 'hr'">
                            <el-input v-model="registerForm.company" autocomplete="off"></el-input>
                        </el-form-item>
						<el-form-item label="用户名/邮箱/手机号" prop="username">
							<el-input v-model="registerForm.username" autocomplete="off"></el-input>
						</el-form-item>
						<el-form-item label="姓名" prop="name">
							<el-input v-model="registerForm.name" autocomplete="off"></el-input>
						</el-form-item>
						<el-form-item label="密码" prop="password">
							<el-input type="password" v-model="registerForm.password" autocomplete="off"></el-input>
						</el-form-item>
						<el-form-item label="确认密码" prop="checkpwd">
							<el-input type="password" v-model="registerForm.checkpwd" autocomplete="off"></el-input>
						</el-form-item>
						<slide-verification @check-result="checkResult"></slide-verification>
						<br />
						<el-button type="primary" @click.native.prevent="handRegister('registerForm')">注册</el-button>
						<div class="text-foot">
							已有账号?
							<router-link to="/login" class="login-link">
								登录
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
			var validatePass = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请输入密码'));
				} else {
					if (this.registerForm.checkpwd !== '') {
						this.$refs.registerForm.validateField('checkpwd');
					}
					callback();
				}
			};
			var validatePass2 = (rule, value, callback) => {
				if (value === '') {
					callback(new Error('请再次输入密码'));
				} else if (value !== this.registerForm.password) {
					callback(new Error('两次输入密码不一致!'));
				} else {
					callback();
				}
			};
			return {
				confirmSuccess: false,
				registerForm: {
					username: null,
					password: null,
					checkpwd: null,
					name: null,
            		role: 'jobseeker',  // Default to job seeker
					company: null  // This will be used if the role is 'hr'
				},
				rules: {
					username: [{
							required: true,
							message: '请输入用户名或邮箱或手机号',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 15,
							message: '长度在 6 到 15 个字符',
							trigger: 'blur'
						}
					],
					password: [{
							required: true,
							message: '请输入密码',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 10,
							message: '长度在 6 到 15 个字符',
							trigger: 'blur'
						},
						{
							validator: validatePass,
							trigger: 'blur'
						}
					],
					checkpwd: [{
							required: true,
							message: '请再次输入密码',
							trigger: 'blur'
						},
						{
							min: 6,
							max: 15,
							message: '长度在 6 到 10 个字符',
							trigger: 'blur'
						},
						{
							validator: validatePass2,
							trigger: 'blur'
						}
					],
					name: [{
							required: true,
							message: '请输入姓名',
							trigger: 'blur'
						},
						{
							min: 2,
							max: 10,
							message: '长度在 2 到 8 个字符',
							trigger: 'blur'
						}
					]
				}
			}
		},
		components: {
			SlideVerification
		},
		methods: {
			//获取滑块验证结果
			checkResult(message) {
				this.confirmSuccess = message
			},
			//处理注册
			handRegister(formName) {
				if (this.confirmSuccess) {
					const msg = this
					this.$refs[formName].validate((valide) => {
						if (valide) {
				            console.log('Sending data:', JSON.parse(JSON.stringify(this.registerForm)));
							axios.post(`api/register/`, this.registerForm).then(res => {
								console.log(res); //处理成功的函数 相当于success
								if (res.status == 200) {
									this.$message({
										message: '注册成功',
										type: 'success'
									});
									this.$router.push('/login')
								} else {
									this.$message({
										message: res.data.msg,
										type: 'error'
									});
								}
							}).catch(function(error) {
								msg.$message('注册失败');
								console.log(error) //错误处理 相当于error
							});
						} else {
							//表单验证失败
							this.$message('请完成表单验证');
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
	#register {
		height: 100vh;
		display: flex;
        align-items: center; // 垂直居中
        justify-content: center; // 水平居中
		/* background-color: #244d6f; */
		background-image: url(../assets/bg.jpg);
		background-repeat: no-repeat;
		background-size: cover;
		background-position: center; // 确保背景图片也居中
	}

    #register-from {
        width: 400px;
        height: 720px;
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

	.el-input {}

    .el-button {
        margin-top: 10px; // 为按钮添加上边距
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
