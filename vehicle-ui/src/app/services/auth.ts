import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AuthService {
  private http = inject(HttpClient);
  private readonly BASE_URL = 'http://127.0.0.1:8000/api';

  register(data: any) {
    return this.http.post(`${this.BASE_URL}/register/`, data);
  }

  login(data: any) {
    return this.http.post(`${this.BASE_URL}/login/`, data);
  }
}
