pipeline {
  agent any
  stages {
    stage('version') {
      steps {
        bat 'python --version'
      }
    }
    stage('parallel test'){
      parallel{
    stage('delay'){  
      steps{
        bat 'timeout /t 20 /nobreak'
      }
    }
    stage('hello') {
      steps {
        bat 'python hello.py'
      }
    }
      }
  }
  }
}
