pipeline {
    agent any

    stages {
        stage('running pipeline'){
            script {
        parallel(
        stage('Generate Chart') {
            steps {
                // Execute the Python script
                
                    bat 'python generate_chart.py'
                }
            
        }
        stage ('real Pipeline')
            {
                steps {

                    bat 'echo 'hello world' '
                }
            
            }    
    )
    }
    }
    }

    post {
       success {
            // Archive the generated chart
           archiveArtifacts artifacts: 'CPUandMemory.png'
           
        }
   }
}
