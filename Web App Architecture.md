# **Web App Architecture & Theory**

## _URL Endpoints_

`https://training.devlaunch.us/tim/?video=123`

- APIs facilitates the access and control of data
- The URL follows the following format: **Domain/path/query_param**
- /tim is the endpoint path and video=123 is the query parameter

## _Request/Response Structure_

| Request Components | Response Components |
| ------------------ | ------------------- |
| Type / Method      | Status Code         |
| Path               | Body                |
| Body               | Headers             |
| Headers            |

### Requests

- Type / Method: (POST, PUT, DELETE, etc.)
- Path: Just the endpoint
- Body: Additional (optional) data to send along with request (images, vids, etc.)
- Headers: Additional information that has to do with things like authentication

### Response

- Status Code: such as 200 (OK) or 404 (Not found)
- Body: Contains additional data to send to the frontend
- Headers: Also related to security/authentication

## _HTTP Methods_

Below is an example for a book api.

- **GET** /books -> Lists all the books in the database
- **DELETE** /books/{bookId} -> Deletes a book based on their id
- **POST** /books -> Creates a book
- **PUT** /books/{bookId} -> Method to update a book
- **GET** /books/{bookId} -> Retrieves a book based on their id

## _Example Request/Response_

### Request Components

**Request Components and Headers**

- Type: PATCH
- Path: /api/post/45535
- Body:

```
{
    "title" : "updated title",
    "description": "I dont like this caption"
}
```

```
{
    "Content-Type" : "application/json",
    "Authorization" : "bearer uenfaouehdflah123124"
}
```

**Response Components and Headers**

- Status Code 204
- Body:

```
{
    "title" : "updated title",
    "description" : "I dont like this caption",
    "postId" : 6767,
    "updatedAt" : "Sept 26, 2025",
    "createdBy" : "user-12345"
}
```

- Headers:

```
{
    "Content-Type" : "application/json"
}
```
