This is a Simple REST based flask API just for learning purpose

With this App Lets also understand few of the important REST principles-

REST- REPRESENTAL STATE TRANSFER
It is a way thinking how a web server behaves or responds to your request
- It does't respond with just data
- It responds with resource 
-REST is stateless - one request can not depend on any other request
-Server only knows about the current request, and not any previous request

REST METHODS:
1.GET/ - Use GET request to get the resource information, 
GET request do not change the state so they are said to be "Safe Methods"
GET API should be idempotent, making GET resource must produce the same result until there is a change in the state of resources
GET response codes - 200(Ok), 404(not found), 400 (bad request)

2.POST/ - Post methods are used to create new resources , POST is neither safe idempotent 
Post response codes  - 201 (created), 200(ok), 204(No content)

3.PUT/ - Put is used to update the existing resource , if resource does not exist then API may decide to create new resource
Put response codes  - 201 (created), 200(ok), 204(No content)

PATCH/- HTTP Patch request are to make partial update on resources, we should only use PUT if we are replacing resource entirety 

DELETE/ - DELETE APIs delete the resources (identified by the Request-URI), DELETE operations are idempotent. If you DELETE a resource, it’s removed from the collection of resources.
Delete response code -

OPTION/ - Identifying which HTTP methods a resource supports.
Allow: OPTIONS, GET, HEAD, POST

HEAD - Same as GET but no response body








