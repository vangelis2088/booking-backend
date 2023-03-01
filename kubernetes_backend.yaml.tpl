apiVersion: apps/v1
kind: Deployment
metadata:
  name: booking-backend
  labels:
    app: booking-backend
spec:
  replicas: 2
  selector:
    matchLabels:
      app: booking-backend
  template:
    metadata:
      labels:
        app: booking-backend
    spec:
      containers:
      - name: booking-backend-app
        # Replace  with your project ID or use `make template`
        image: us-central1-docker.pkg.dev/gifted-cooler-378519/backend-repository/booking-backend-app:COMMIT_SHA
        # This setting makes nodes pull the docker image every time before
        # starting the pod. This is useful when debugging, but should be turned
        # off in production.
        env:
            - name: DATABASE_NAME
              valueFrom:
                secretKeyRef:
                  name: cloudsql
                  key: database
            - name: DATABASE_USER
              valueFrom:
                secretKeyRef:
                  name: cloudsql
                  key: username
            - name: DATABASE_PASSWORD
              valueFrom:
                secretKeyRef:
                  name: cloudsql
                  key: password
        ports:
        - containerPort: 5000

      - image: gcr.io/cloudsql-docker/gce-proxy:1.16
        name: cloudsql-proxy
        command: ["/cloud_sql_proxy", "--dir=/cloudsql",
                  "-instances=gifted-cooler-378519:us-central1:booking=tcp:5432",
                  "-credential_file=/secrets/cloudsql/credentials.json"]
        volumeMounts:
          - name: cloudsql-oauth-credentials
            mountPath: /secrets/cloudsql
            readOnly: true
          - name: ssl-certs
            mountPath: /etc/ssl/certs
          - name: cloudsql
            mountPath: /cloudsql
      volumes:
        - name: cloudsql-oauth-credentials
          secret:
            secretName: cloudsql-oauth-credentials
        - name: ssl-certs
          hostPath:
            path: /etc/ssl/certs
        - name: cloudsql
          emptyDir: {}