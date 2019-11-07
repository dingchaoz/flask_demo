# flask_demo

# Usage 
1. Pickle dump the model file, and replaced the file path in server.py, and make necessary changes in that script to make the new model work
2. Update the requirements.txt if there are particular pacakges needed for the ml model such as sklearn
3. Run the following lines to start the mo
```
cd ml_api
docker build -t test_ml_api .  
docker run --rm -p 5000:8080 test_ml_api
```
4. Start a new terminal to fire curl message to ping the docker api, example message is following: 
```

```
