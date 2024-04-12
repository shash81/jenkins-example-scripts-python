pipeline {
    agent any

    stages {
        stage('Generate Chart') {
            steps {
                // Execute the Python script
                script {
                    bat 'python generate_chart.py'
                }
            }
        }
    }

    post {
       success {
            // Archive the generated chart
           archiveArtifacts artifacts: 'cpu_chart.png'
           archiveArtifacts artifacts: 'memory_chart.png'
        }
   }
}
