pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                sh 'python hola_mundo.py' // En Windows: bat 'python hola_mundo.py'
            }
        }
    }
}