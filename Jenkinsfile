
def getHostname(String domain, String project, String branch_name=null) {
    elements = [project, domain]
    if (branch_name) {
        elements.add(0, branch_name);
    }
    return elements.join('.')
}

env.NORMALIZED_BRANCH_NAME = env.BRANCH_NAME.replaceAll('/', '--');
env.DEFAULT_BRANCH = 'master'
env.PROJECT_NAME = 'beerdiary_server'
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

node {
    stage('Checkout') {
        checkout scm
    }

    /*
        @TODO

        Tests should be running without service containers (DB, cache, etc.).
        A service providing instances of these is required. Examples:
         - https://wiki.openstack.org/wiki/Trove
         - https://mktmp.io/
        Then, project should all to be configured using 12factor-style
        environment variables.

    stage('Development container setup') {
        sh 'docker-compose -f test.yml build'
    }
    */

    stage('Image') {
        sh 'docker-compose build'
        sh 'docker-compose push'
    }

    stage('Deployment') {
        sh 'docker stack deploy --compose-file ./docker-compose.yml $BUILD_NAME'
    }
}