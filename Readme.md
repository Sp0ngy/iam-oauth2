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
- `curl -H "Headerinformation: XYZ" -d "data1=myname&data2=unicorn" "myurl:8000/whatever"`

# OAuth 2.0 for Browser-Based for First-Party Apps
Reference: [Datatracker](https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#name-first-party-applications)
- MUST: Usage of redirect-flow --> OAuth Authorization Code flow
- MUST: Implementation of Proof Key for Code Exchange (PKCE [RFC7636])

# django-oauth-toolkit url
[127.0.0.1:8000/o/applications/]() -> register & edit apps