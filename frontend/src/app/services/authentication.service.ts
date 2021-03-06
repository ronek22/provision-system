import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { ConfigurationService } from './configuration.service';
import { ReplaySubject, Observable, of, BehaviorSubject } from 'rxjs';
import { map } from 'rxjs/operators';
import { NgForm } from '@angular/forms';


@Injectable({
  providedIn: 'root'
})
export class AuthenticationService {
  isRequesting: boolean = false;
  isLoggedIn = new BehaviorSubject<boolean>(false);

  constructor(private http: HttpClient, private configurationService: ConfigurationService) {
      this.checkIfUserInLocalStorage();
   }

   login(username: string, password: string) {
     return this.http.post<any>(`${this.configurationService.apiUrl}/accounts/login`, {username, password})
      .pipe(map(user => {
        // login successful if there's a jwt token in the response
        if (user && user.access_token) {
          // store user details and jwt token in local storage to keep user logged in between page refreshes
          localStorage.setItem('currentUser', JSON.stringify(user));
          this.isLoggedIn.next(true);
        }

        return user.user;
      }));
   }


   register(form: NgForm) {
     return this.http.post<any>(`${this.configurationService.apiUrl}/accounts/register`, form);
   }

   logout() {
     // remove user from local storage to log out
     localStorage.removeItem('currentUser');
     localStorage.removeItem('refreshtoken');
     this.isLoggedIn.next(false);
   }

   refreshToken() {
     return this.http.post<any>(`${this.configurationService.apiUrl}/accounts/refresh`, {});
   }

   validateUsername(username: string) {
     return this.http.post<any>(`${this.configurationService.apiUrl}/accounts/validate-username`, {'username': username});
   }

   changeStatus(): Observable<boolean> {
     this.isRequesting = true;
     return of(this.isRequesting);
   }

   private checkIfUserInLocalStorage() {
     let currentUser = JSON.parse(localStorage.getItem('currentUser'));
     if (currentUser) {
       this.isLoggedIn.next(true);
     }
     else {
       this.isLoggedIn.next(false);
     }
   }
}

