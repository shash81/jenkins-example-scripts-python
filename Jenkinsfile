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

  //  post {
  //      success {
            // Archive the generated chart
          //  archiveArtifacts artifacts: 'sample_chart.png'
       // }
   // }
}
