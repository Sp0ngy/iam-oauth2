from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny

import requests

from users.serializer import CreateUserSerializer

CLIENT_ID = 'Zl5jJTtI1EHaU86veg000Jla8INBMYAlCvVArAqb'
CLIENT_SECRET = 'oC838JkGF0ts3sA9IX5ejrLAdTmgdMS664jIBTrOrM6Pk13aq7JFypga1f9TQ89xaduThza97UPer4sSMQntS88BEkcZDnEychhzrDIfR7IgNW51kJPyUhkZ4aIPNM5Z'


# TODO: First-Party Applications MUST NOT use "resource owner password credentials grant" --> change to "authorization
# code flow", see https://datatracker.ietf.org/doc/html/draft-ietf-oauth-browser-based-apps#name-first-party-applications


@api_view(['POST'])
@permission_classes([AllowAny])
def register(request):
    '''
    Registers user to the server. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    # Put the data from the request into the serializer
    serializer = CreateUserSerializer(data=request.data)

    # Validate the data
    if serializer.is_valid():
        # If it is valid, save the data (creates a user).
        serializer.save()
        # Then we get a token for the created user.
        # This could be done differently
        r = requests.get('http://127.0.0.1:8000/o/token/',
                          data={
                              'response_type': 'code',
                              'client_id': CLIENT_ID,
                              'redirect_uri': 'http://127.0.0.1:8000/noexist/callback',
                          },
                          headers={
                              'content-type': "application/x-www-form-urlencoded",
                              'cache-control': "no-cache",
                          },
                          )
        print(r)
        return Response(r.json())
    return Response(serializer.errors)


@api_view(['POST'])
@permission_classes([AllowAny])
def token(request):
    '''
    Gets tokens with username and password. Input should be in the format:
    {"username": "username", "password": "1234abcd"}
    '''
    r = requests.post(
        'http://localhost:8000/o/token/',
        data={
            'grant_type': 'password',
            'username': request.data['username'],
            'password': request.data['password'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def refresh_token(request):
    '''
    Registers user to the server. Input should be in the format:
    {"refresh_token": "<token>"}
    '''
    r = requests.post(
        'http://localhost:8000/o/token/',
        data={
            'grant_type': 'refresh_token',
            'refresh_token': request.data['refresh_token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    return Response(r.json())


@api_view(['POST'])
@permission_classes([AllowAny])
def revoke_token(request):
    '''
    Method to revoke tokens.
    {"token": "<token>"}
    '''
    r = requests.post(
        'http://localhost:8000/o/revoke_token/',
        data={
            'token': request.data['token'],
            'client_id': CLIENT_ID,
            'client_secret': CLIENT_SECRET,
        },
    )
    # If it goes well return sucess message (would be empty otherwise)
    if r.status_code == requests.codes.ok:
        return Response({'message': 'token revoked'}, r.status_code)
    # Return the error if it goes badly
    return Response(r.json(), r.status_code)
