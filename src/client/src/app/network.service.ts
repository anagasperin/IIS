import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { lastValueFrom, Observable } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root',
})
export class NetworkService {
  constructor(private httpClient: HttpClient) {}

  getCurrentWeather(): Observable<any> {
    const lat = '46.05';
    const lon = '14.51';
    const key = '87c05a0a8d8ea08172b92485c4a60cde';
    const url = `https://api.openweathermap.org/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${key}&units=metric`;
    return this.httpClient.get<any>(url).pipe(
      catchError((error): any => {
        alert('Network error');
        return { error: error };
      })
    );
  }

  getAirPollution(): Observable<any> {
    const lat = '46.05';
    const lon = '14.51';
    const key = '87c05a0a8d8ea08172b92485c4a60cde';
    const url = `http://api.openweathermap.org/data/2.5/air_pollution?lat=${lat}&lon=${lon}&appid=${key}`;
    return this.httpClient.get<any>(url).pipe(
      catchError((error): any => {
        alert('Network error');
        return { error: error };
      })
    );
  }

  getForecast(): Observable<any> {
    const url = 'http://localhost:5000/forecast';
    return this.httpClient.get<any>(url).pipe(
      catchError((error): any => {
        alert('Network error');
        console.log(error);
        return { error: error };
      })
    );
  }
}
