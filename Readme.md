# OAuth2 Protocol
     +--------+                               +---------------+
     |        |--(A)- Authorization Request ->|   Resource    |
     |        |                               |     Owner     |
     |        |<-(B)-- Authorization Grant ---|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(C)-- Authorization Grant -->| Authorization |
     | Client |                               |     Server    |
     |        |<-(D)----- Access Token -------|               |
     |        |                               +---------------+
     |        |
     |        |                               +---------------+
     |        |--(E)----- Access Token ------>|    Resource   |
     |        |                               |     Server    |
     |        |<-(F)--- Protected Resource ---|               |
     +--------+                               +---------------+
                     Figure 1: Abstract Protocol Flow

    +--------+                                           +---------------+
    |        |--(A)------- Authorization Grant --------->|               |
    |        |                                           |               |
    |        |<-(B)----------- Access Token -------------|               |
    |        |               & Refresh Token             |               |
    |        |                                           |               |
    |        |                            +----------+   |               |
    |        |--(C)---- Access Token ---->|          |   |               |
    |        |                            |          |   |               |
    |        |<-(D)- Protected Resource --| Resource |   | Authorization |
    | Client |                            |  Server  |   |     Server    |
    |        |--(E)---- Access Token ---->|          |   |               |
    |        |                            |          |   |               |
    |        |<-(F)- Invalid Token Error -|          |   |               |
    |        |                            +----------+   |               |
    |        |                                           |               |
    |        |--(G)----------- Refresh Token ----------->|               |
    |        |                                           |               |
    |        |<-(H)----------- Access Token -------------|               |
    +--------+           & Optional Refresh Token        +---------------+
                 Figure 2: Refreshing an Expired Access Token

# cURL (client URL) Commands
- `curl -d "data1=myname&data2=unicorn" "myurl:8000/whatever" posts -data to url`
- `curl -H "Headerinformation: XYZ" adds -Header information`
- `curl -X POST -H "Cache-Control: no-cache" -H "Content-Type: application/x-www-form-urlencoded" "http://127.0.0.1:8000/o/token/" -d "client_id=Zl5jJTtI1EHaU86veg000Jla8INBMYAlCvVArAqb" -d "client_secret=oC838JkGF0ts3sA9IX5ejrLAdTmgdMS664jIBTrOrM6Pk13aq7JFypga1f9TQ89xaduThza97UPer4sSMQntS88BEkcZDnEychhzrDIfR7IgNW51kJPyUhkZ4aIPNM5Z" -d "code=ZDAFyShtMip68h6i6Hqtmk9z67p0BN" -d "code_verifier=WjhLNTE5M1pKWFhVVE1XNDhZMllKNDYySlAyREtSUDFLODYwNFdYRFRaWkJNOFlQMUUyWVNEM1M3RDA4RkZEVVFYMkk3N05JWThDUzdFSFUwSVI" -d "redirect_uri=http://127.0.0.1:8000/noexist/callback" -d "grant_type=authorization_code"`

# OAuth 2.0 for Browser-Based for First-Party Apps
Reference: [Datatracker](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#name-first-party-applications)
- MUST: Usage of redirect-flow --> OAuth Authorization Code flow
- MUST: Implementation of Proof Key for Code Exchange (PKCE [RFC7636])

# django-oauth-toolkit url
[127.0.0.1:8000/o/applications/]() -> register & edit apps

# Error causes
`"error": "invalid_grant"` 
- Grant expired, check localhost:8000/admin -> Grants -> set expiration date
- incorrect `client_id`, `code_verifier` or `code`

`"error": "unsupported_grant_type"`
- POST request on `"grant_type": "authorization_code"`
- **PS (personal stupidity)**