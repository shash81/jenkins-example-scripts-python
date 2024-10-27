pipeline {
    agent any

    stages {
      
               
       
        stage('Generate Chart') {
            steps {
                // Execute the Python script
                
                    bat 'python generate_chart.py'
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
