import { Component, inject } from '@angular/core'; // Added inject
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';
import { HttpClient } from '@angular/common/http';
import { RouterLink } from "@angular/router";
import { AuthService } from '../services/auth';

@Component({
  selector: 'app-register',
  standalone: true,
  imports: [CommonModule, FormsModule, RouterLink], 
  templateUrl: './register.html',
  styleUrl: './register.css',
})
export class Register {
  // Use inject() for a cleaner, modern dependency injection
  private http = inject(HttpClient);

  first_name = '';
  middle_name = '';
  last_name = '';
  email = '';
  phone = '';
  password = '';
  error = '';
  success = '';
  loading = false;

  private readonly API_URL = 'http://127.0.0.1:8000/api/register/';
  private authService = inject(AuthService);

  register(){
    if (this.loading) return;
    this.loading = true;

    this.authService.register({
      first_name: this.first_name,
      middle_name: this.middle_name,
      last_name: this.last_name,
      email: this.email,
      phone: this.phone,
      password: this.password
    }).subscribe({
      next: () => {
        this.success = "Registration successful";
        this.loading = false;
        this.resetForm();
      },
      error: (err: any) => {
        this.loading = false;
        this.handleError(err);
      }
    })

  }



  private handleError(err: any) {
    if (err.error?.email) {
      this.error = Array.isArray(err.error.email) ? err.error.email[0] : err.error.email;
    } else if (err.error?.error) {
      this.error = err.error.error;
    } else {
      this.error = 'Registration failed. Please check your details.';
    }
  }

  private resetForm() {
    this.first_name = '';
    this.middle_name = '';
    this.last_name = '';
    this.email = '';
    this.phone = '';
    this.password = '';
  }
}