#!/usr/bin/env groovy

properties([[
    $class: 'BuildDiscarderProperty',
    strategy: [$class: 'LogRotator', artifactDaysToKeepStr: '', artifactNumToKeepStr: '', daysToKeepStr: '', numToKeepStr: '10']
]])


node("linux&&!LINUX_DEDEV10UBB64V16&&!LINUX_DEDEV10UBB64V17")
{
    try {
        stage('SCM')
        {
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
    finally
    {
        cleanWs()
    }
}
