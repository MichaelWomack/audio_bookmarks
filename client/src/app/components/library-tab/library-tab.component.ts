import { Component, OnInit } from '@angular/core';
import { AudioInfo } from './../../model/audio-info';

@Component({
  selector: 'app-library-tab',
  templateUrl: './library-tab.component.html',
  styleUrls: ['./library-tab.component.scss']
})
export class LibraryTabComponent implements OnInit {

  private audio1: AudioInfo = {
    audioName: 'The Intelligent Investor',
    audioAuthor: 'Benjamin Graham'
  };

  private audio2: AudioInfo = {
    audioName: 'Security Analysis',
    audioAuthor: 'Benjamin Graham'
  };

  private audio3: AudioInfo = {
    audioName: 'Investing Again',
    audioAuthor: 'Benjamin Graham'
  };

  constructor() {

  }

  ngOnInit() {
  }

}
