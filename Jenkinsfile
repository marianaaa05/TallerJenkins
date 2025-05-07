pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                bat 'python hola_mundo.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                bat 'pytest test_hola_mundo.py'
            }
        }
    }
}