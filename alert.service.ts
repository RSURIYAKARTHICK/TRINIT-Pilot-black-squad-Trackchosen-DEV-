// alert.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
    providedIn: 'root'
})
export class AlertService {
    private apiUrl = 'http://localhost:8000/api/alerts/';

    constructor(private http: HttpClient) { }

    getAlerts() {
        return this.http.get(this.apiUrl);
    }
}
