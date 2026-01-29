import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root',
})
export class Auth {
  private  API_URL = 'http://localhost:8000/api/auth';

  constructor(private http: HttpClient) {}

  login(email:string, password:string){
    return this.http.post(`${this.API_URL}/login`,{
      email,
      password
    });
  }

  saveToken(token: string){
    localStorage.setItem('access_token',token);
  }

  getToken(){
    return localStorage.getItem('access_token');
  }

  logout(){
    localStorage.removeItem('accessToken');
  }


}

