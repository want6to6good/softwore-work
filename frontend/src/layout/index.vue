<template>
	<div id="layout">
		<el-container>
			<el-header>
				<el-row type="flex" justify="space-between">
					<a href="/"><img src="@/assets/logo.png" height="50px" /></a>
					<el-menu :default-active="activeIndex" class="el-menu-title" mode="horizontal" @select="handleSelect"
					 background-color="#ffffff" text-color="#85baef" active-text-color="#1884f2" :router="true">
						<el-menu-item index="/job">职位市场</el-menu-item>
						<el-menu-item index="/resume">简历</el-menu-item>
						<el-menu-item index="/message">消息</el-menu-item>
						<!-- <el-menu-item index="/mistake" disabled>模拟面试</a></el-menu-item> -->
						<el-menu-item index="/interview">模拟面试</a></el-menu-item>
					</el-menu>
					<el-dropdown>
						<span class="el-dropdown-link" style="height: 50px;">
							<el-row>
								<span>
									<i class="el-icon-user-solid"></i>
									<span>{{getStudent.name}}</span>
									<i class="el-icon-arrow-down el-icon--right"></i>
								</span>
							</el-row>
						</span>
						<el-dropdown-menu slot="dropdown">
							<el-dropdown-item>
								<el-button type="text" @click="toCenter">个人中心</el-button>
							</el-dropdown-item>
							<el-dropdown-item>
								<el-button type="text" @click="toUpdatePwd">修改密码</el-button>
							</el-dropdown-item>
							<el-dropdown-item divided>
								<el-button type="text" @click="loginOut">退出登录</el-button>
							</el-dropdown-item>
						</el-dropdown-menu>
					</el-dropdown>
				</el-row>
			</el-header>
			<el-main>
				<router-view />
			</el-main>
			<el-footer>
				<b>@Copyright 2023-2024. ALL Rights Reserved</b>
			</el-footer>
		</el-container>
	</div>
</template>

<script>
	export default {
		name: "layout",
		data() {
			return {
				activeIndex: this.$route.path
			};
		},
		computed: {
			getStudent() {
    			return this.$store.state.student || { name: 'TODO: Name' };
			}
		},
		methods: {
			handleSelect(key, keyPath) {
				//console.log(key, keyPath);
				this.activeIndex = key
			},
			loginOut() {
				//console.log("before:" + localStorage.getItem('Authorization'))
				localStorage.clear()
				sessionStorage.clear()
				//console.log("after" + localStorage.getItem('Authorization'))
				this.$router.push('/login');
			},
			toCenter() {
				this.$router.push({
					name: 'Center',
					params: {}
				});
			},
			toUpdatePwd() {
				this.$router.push({
					name: 'Password',
					params: {}
				});
			}
		},
		created() {

		}
	}

</script>

<style lang="scss" scoped>
#layout {
  max-width: 1200px; // 最大宽度
  width: 100%; // 宽度设置为100%，允许在小屏幕上自动调整大小
  margin: 0 auto; // 水平居中
  padding: 0 20px; // 增加一些内边距保证内容不会紧贴屏幕边缘

  .el-header {
    border-bottom: 1px solid #e6e6e6;
  }

  .el-main {
    min-height: 100%; // 保持最小高度
  }

  .el-footer {
    // 如有需要，这里也可以添加样式
  }

  .el-dropdown img {
    margin-top: 10px; // 调整图片的上边距，适用于下拉菜单中的头像或其他图标
  }

  .el-menu-item {
    font-size: 18px; // 调整菜单项字体大小，保持清晰可读
  }

  .el-dropdown {
    margin-top: 10px; // 下拉菜单顶部的外边距
  }

  .el-dropdown-link {
    cursor: pointer; // 确保鼠标悬停时显示指针
    color: #909090; // 字体颜色
    font-size: 18px; // 字体大小
  }

  .el-icon-arrow-down {
    font-size: 18px; // 箭头图标的大小，与菜单字体大小一致
  }
}
</style>