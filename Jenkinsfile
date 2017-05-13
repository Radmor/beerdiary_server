@Library('shared')
import gd.mrx.ci.DockerStack

node {
    stage('Checkout') {
        checkout scm
    }

    def stack = new gd.mrx.ci.DockerStack(this, 'beerdiary_server')
    stack.execute()

    stage('Test'){

    env.NORMALIZED_BRANCH_NAME = env.BRANCH_NAME.replaceAll('/', '--'); 
    env.DEFAULT_BRANCH = 'master' 
    env.PROJECT_NAME = 'beerdiary_server_test' 
    env.REPOSITORY_URL = 'localhost:5000' 
    env.DOMAIN = 'ci.devmerix.com' 
    env.COMPOSE_ENV_FILE = '.env.jenkins' 
    
    if (env.BRANCH_NAME != env.DEFAULT_BRANCH) { 
        env.BUILD_NAME = env.PROJECT_NAME + '-' + env.NORMALIZED_BRANCH_NAME 
    } else { 
        env.BUILD_NAME = env.PROJECT_NAME 
    } 
    env.DEPLOY_HOSTNAME = getHostname( 
        env.DOMAIN, 
        env.PROJECT_NAME, 
        env.BRANCH_NAME == env.DEFAULT_BRANCH ? env.BRANCH_NAME : null) 
    
    sh 'docker-compose -f test.yml build'
    }
}