pipeline {
  agent any

  environment {
    NEXUS_USER = 'admin'
    NEXUS_PASSWORD = '30a75904-f7aa-42aa-aeb0-94b4cdcddad0'
    NEXUS_URL = "localhost:8081"
    NEXUS_REPOSITORY = "JIAM"
	NEXUS_REPO_ID    = "vprofile-release"   
    NEXUS_IP = "127.0.0.1"
    NEXUS_POST = "8081"
    NEXUS_LOGIN = "nexus_user"
    SONARSERVER = "sonarserver"
    SONARSCANNER = "sonnarscanner"
  }
 
  stages {
    stage('uploadFile') {
      steps {
       nexusArtifactUploader(
        nexusVersion: 'nexus3',
        protocol: 'http',
        nexusUrl: "${NEXUS_IP}:${NEXUS_PORT}",
        groupId: 'QA',
        version: "1.0",
        repository: 'RepositoryName',
        credentialsId: ${NEXUS_LOGIN},
        artifacts: [
            [artifactId: 'jiamapp',
             classifier: '',
             file: 'target/my-service-' + version + '.zip',
             type: 'zip']
        ]
     )
    }
    }
  }
}