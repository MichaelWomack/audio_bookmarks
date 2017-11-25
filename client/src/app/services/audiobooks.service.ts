import {Injectable} from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';
import {Observable} from 'rxjs/Observable';
import {Audiobook} from '../model/audiobook';

@Injectable()
export class AudiobooksService {

  constructor(private http: HttpClient) {
  }

  getAudiobooks(): Observable<Audiobook[]> {
      return this.http.get<Audiobook[]>(`/api/audiobooks`);
  }
}
