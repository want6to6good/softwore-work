<template>
	<div id="job">
		<el-row type="flex" justify="center">
			<el-col :span="4">
				<el-input v-model="key" placeholder="请输入职位名称" prefix-icon="el-icon-search" clearable></el-input>
			</el-col>
			<el-col :span="4">
				<el-button type="primary" @click="searchJob()">搜索职位</el-button>
			</el-col>
		</el-row>
		<el-row>
			<h1>职位列表</h1>
			<div style="padding-left: 0px">
				<el-col :span="4" v-for="(item, index) in pagination.results" :key="index" :offset="index > 0 ? 1 : 0">
					<el-card :body-style="{ padding: '0px' }" v-loading="loading">
						<div style="padding: 14px;">
							<span>职位：{{ item.title }}</span>
							<p>描述：{{ item.description }}</p> <!-- 添加工作描述 -->
							<p>公司：{{ item.company_name }}</p> <!-- 添加公司 ID -->
							<p>发布日期：{{ item.posted_date }}</p> <!-- 调整字段名以匹配新的数据结构 -->
							<p>地点：{{ item.location }}</p>
							<p>薪资：{{ item.salary }}</p> <!-- 添加薪资信息 -->
							<div class="bottom clearfix">
								<el-button type="text" class="button" @click="applyToJob(index)">申请</el-button>
							</div>
						</div>
					</el-card>
				</el-col>
			</div>
		</el-row>
		<Pagination :count="pagination.count" @size-change="handleSizeChange" @current-change="handleCurrentChange"></Pagination>
	</div>
</template>

<script>
import Pagination from '@/components/Pagination.vue'
export default {
	data() {
		return {
			loading: false,
			key: null,
			page: 1,
			page_size: 5,
			pagination: {
				count: null,
				next: null,
				previous: null,
				results: []
			}
		}
	},
	components: {
		Pagination
	},
	computed: {
		username() {
			return this.$store.state.user.username;
		}
	},
	methods: {
		getJobInfo() {
			console.log(this.page)
			console.log(this.page_size)

			this.$axios(`/api/job/?format=json`, {
				params: {
					page: this.page,
					page_size: this.page_size,
				}
			}).then(res => {
				console.log(res.data);
				this.pagination.results = res.data;
				this.loading = false;
			}).catch(error => {
				console.log(error);
				this.loading = false;
			});
		},
		handleSizeChange(val) {
			this.page_size = val
			this.searchJob()
		},
		handleCurrentChange(val) {
			this.page = val
			this.searchJob()
		},
		searchJob() {
			if (this.key) {
				this.$axios(`/api/job/?format=json`, {
					params: {
						page: this.page,
						page_size: this.page_size,
						search: this.key,
						// student_id: this.$store.state.user.id,
					}
				}).then(res => {
					if (res.status == 200) {
						this.pagination = res.data
					}
				})
			} else {
				this.getJobInfo()
			}
		},
		applyToJob(index) {
			localStorage.removeItem('job');
			localStorage.setItem("job", JSON.stringify(this.pagination.results[index]));
			
			const job = this.pagination.results[index];
			const jobname = job.title;
			const username = this.username;

			this.$axios(`/api/application_create/?format=json`, {
				params: {
					jobname: jobname,
					username: username
				}
			}).then(response => {
					this.$message.success('Application submitted successfully!');
					console.log(response.data);
				})
				.catch(error => {
					this.$message.error('Failed to submit application.');
					console.error(error);
				});
			}
	},
	created() {
		this.loading = true;
	    this.getJobInfo();  // 调用获取职位信息的方法
		setTimeout(() => {  // 假设加载是异步的，这里用 setTimeout 模拟异步加载结束
			this.loading = false
		}, 1000);
	}
}
</script>






<style lang="scss" scoped>
    #job {
        margin-top: 10px;
        display: flex; // 设置为flex布局
        // align-items: center; // 子元素水平居中

        flex-direction: column; // 子元素垂直排列
    }
    
	.bottom {
		margin-top: 13px;
		line-height: 12px;
	}

	.button {
		padding: 0;
	}

	.image {
		width: 50%;
		height: 80%;
		display: block;
		margin: 20px auto 10px auto;
	}

	.clearfix:before,
	.clearfix:after {
		display: table;
		content: "";
	}

	.clearfix:after {
		clear: both;
	}
</style>