pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                echo 'Construyendo el proyecto...'
                bat 'python holaMundo.py'
            }
        }
        stage('Test') {
            steps {
                echo 'Ejecutando pruebas...'
                bat 'python test_hola_mundo.py'
            }
        }
    }
}