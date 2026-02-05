import { ApplicationConfig, provideBrowserGlobalErrorListeners } from '@angular/core';
import { provideRouter } from '@angular/router';
import { provideHttpClient, withFetch } from '@angular/common/http'; // Added this
import { provideClientHydration, withEventReplay } from '@angular/platform-browser';
import { routes } from './app.routes';

export const API_BASE_URL = 'http://127.0.0.1:8000';

export const appConfig: ApplicationConfig = {
  providers: [
    provideRouter(routes),
    provideHttpClient(withFetch()), // Enables modern Fetch API for HttpClient
    provideClientHydration(withEventReplay()),
    provideBrowserGlobalErrorListeners(),
  ]
};