# enginf_exercise
Here's my attempt at the exercise provided in the enginf_exercise. I made all my own stuff. It's not perfect, but It was fun and I learned a few things on the way 😊

To run this locally, you'll first need an API_KEY from https://openweathermap.org/api. These guys had a simple API that was super easy to use and most importantly FREE!

Other then that, everything should work out of the box. 


Docker execution:
docker build . -t enginf_exercise && docker run -p 5000:5000 enginf_exercise && docker run enginf_exercise

Kubernetes execution:
kubectl apply -f deployment.yml
kubectl apply -f service.yml

Taking down kubernetes deployment:
kubectl delete deployment DEPLOYMENT_NAME
kubectl delete service SERVICE NAME

