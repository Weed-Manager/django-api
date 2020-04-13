# Strains
Supports getting a list, getting a detailed object, creating and destroying strains 

## Creating a new strain

**Request**:

POST /strains/

Parameters:

Name       | Type   | Required | Description
-----------|--------|----------|------------
name	   | string | Yes      | The strain name
quantity   | float  | Yes      | The strain's initial quantity.

*Note:*

- Authorization protected
- Will get the user by its token
- **The initial quantity will be added as a positive strain operation**
- You can't have two strains with the same name per user


**Response**:

```json
Content-Type application/json
201 Created

{
  "id": "1",
  "strain_name": "Lemon Haze",
  "quantity": "30"
}
```

## Getting a strain

**Request**:

DELETE /strains/{strain_id}

Parameters:

NONE
		
*Note:*

- Authorization protected


**Response**:

```json
Content-Type application/json
204 NO CONTENT 

{
    "id": 1,
    "strain_name": "Lemon Haze",
    "quantity": -0.15
}
```

## Deleting a strain

**Request**:

DELETE /strains/{strain_id}

Parameters:

NONE
		
*Note:*

- Authorization protected
- Only the user can delete its strain


**Response**:

```json
Content-Type application/json
204 NO CONTENT 

{
}
```

