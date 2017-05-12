@Library('shared')
import gd.mrx.ci.DockerStack

node {
    stage('Checkout') {
        checkout scm
    }

    def stack = new gd.mrx.ci.DockerStack(this, 'beerdiary_server')
    stack.execute()
}