# store_api_test-assigment

## Test assignment for a developer vacancy. 
The app is API for a shop where you can get list of products and product information page.


#### The app is written using DJANGO, DJANGO REST FRAMEWORK.


#### WEB API ROUTING TABLE:

| route:  | HTTP methods: | action: |
| ------------- |:-------------:|-------------|
| api/products/ | GET | getting a list of all prodcuts |
| api/products/id | GET | getting product details |


#### LOCAL RUNNING INSTRUCTION:

1. To copy git repository to the local machine, run:

```bash
git clone https://github.com/a500309191/store_api_test-assigment
```
2. To run containers:

```bash
docker-compose up
```


#### ADMIN PAGE: http://localhost:8000/admin/ 

*by docker-compose up command superuser will create automatically*

**login/password: admin**

products data is provided in JSON format:

![Image alt](https://github.com/a500309191/store_api_test-assigment/blob/main/readme_images/product_list_screenshot.JPG)

uploaded image automatically saved in two formats: original (png, jpeg) and webp.

By key "path" you can get relative path to image. Add format at the end of the path and get image

