# REST API

## 🌐 API Basics

#### 🧩 What is an API?

**API** stands for **Application Programming Interface**.\
It allows different applications — even if they’re built using different technologies — to **communicate** with each other.

***

#### 🔄 How It Works

* Usually follows a **client–server** model.
* The **client** requests data, and the **server** responds.
* The data is often returned in **JSON** format (JavaScript Object Notation).

***

#### 💡 JSON (JavaScript Object Notation)

* A lightweight format used to represent data as **key–value pairs**.
* Example:

```json
{
  "id": 5,
  "name": "Latte",
  "price": 120
}
```

So, **JSON** is the _language_ of data exchange, and **API** is the _interface_ that allows this exchange.

***

#### ⚙️ API Endpoints

An **endpoint** is a specific URL through which the client accesses data from the server.\
Example:

```
/drinks
/drinks/5
```

Here, `/drinks/5` might fetch data about a specific drink with ID `5`.

***

#### 🌍 REST APIs

**REST** stands for **Representational State Transfer** — a common way to structure and communicate over the web using APIs.

Example:

* Suppose we have a backend server written in **Python**.
* It communicates with a **database**, but we don’t give users direct DB access.
* Instead, we expose **API endpoints** like:

```
GET /api/drinks
GET /api/drinks/5
```

These endpoints return structured **JSON responses** containing the requested data.

***

#### 🚀 Summary

| Term | Full Form                         | Purpose                           |
| ---- | --------------------------------- | --------------------------------- |
| API  | Application Programming Interface | Enables app-to-app communication  |
| JSON | JavaScript Object Notation        | Data format for API communication |
| REST | Representational State Transfer   | Defines how web APIs communicate  |

#### 🔐 Public vs Private APIs

* **Public API:**\
  Anyone can use it — often provided by companies to integrate their services (e.g., weather APIs, map APIs).
* **Private API:**\
  Restricted access. You can still use it, but only with **proper authentication** (like **OAuth2** tokens or API keys).

***

#### ⚙️ Common HTTP Methods

| Method     | Purpose              | Description                        |
| ---------- | -------------------- | ---------------------------------- |
| **GET**    | Retrieve data        | Used to fetch data from the server |
| **POST**   | Create new data      | Adds new entries to the database   |
| **PUT**    | Update existing data | Modifies an existing record        |
| **DELETE** | Remove data          | Deletes a record from the database |

***

#### 🧱 CRUD Operations

**CRUD** stands for the four basic actions you can perform on a database:

| Operation  | HTTP Method | Description                   |
| ---------- | ----------- | ----------------------------- |
| **Create** | `POST`      | Add a new record              |
| **Read**   | `GET`       | Retrieve existing records     |
| **Update** | `PUT`       | Modify existing data          |
| **Delete** | `DELETE`    | Remove data from the database |

***

#### ⚔️ PUT vs POST

| Aspect               | PUT                                            | POST                                     |
| -------------------- | ---------------------------------------------- | ---------------------------------------- |
| **Purpose**          | Update existing data                           | Create new data                          |
| **Example Endpoint** | `PUT /drinks/605`                              | `POST /drinks`                           |
| **Idempotency**      | ✅ Yes (repeated calls don’t change the result) | ❌ No (each call can create a new record) |

> **Idempotent** means that performing the same operation multiple times produces the same result.

\


