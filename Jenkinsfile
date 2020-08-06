#!/usr/bin/env groovy

node("linux&&!LINUX_DEDEV10UBB64V16&&!LINUX_DEDEV10UBB64V17")
{
    stage('SCM') {
        checkout scm
    }
    stage('Generate documentation') {
        sh """
            cd tjf
            chmod 777 ./create_docs.sh
            ./create_docs.sh
        """
    }
    stage('Upload docs')
    {
        sh """
            cd tjf
            scp -r docs ci-slave@deployment.cds.testo:/deployment/data/docs/mobileapps/tjf
        """
    }
}
