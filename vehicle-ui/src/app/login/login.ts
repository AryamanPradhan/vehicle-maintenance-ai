import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RouterLink, Router } from "@angular/router";

@Component({
  selector: 'app-login',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink],
  templateUrl: './login.html',
  styleUrl: './login.css',
})
export class Login {
  private http = inject(HttpClient);
  private router = inject(Router);

  email = '';
  password = '';
  rememberMe = false;
  
  error = '';
  loading = false;

  private readonly API_URL = 'http://127.0.0.1:8000/api/login/';

  onLogin() {
    this.error = '';
    this.loading = true;

    const payload = {
      email: this.email,
      password: this.password
    };

    this.http.post<any>(this.API_URL, payload).subscribe({
      next: (res) => {
        this.loading = false;
        // Save token to localStorage if your API returns one
        if (res.token) localStorage.setItem('token', res.token);
        this.router.navigate(['/dashboard']);
      },
      error: (err) => {
        this.loading = false;
        this.error = err.error?.message || 'Invalid email or password.';
      }
    });
  }
}