import { Component, OnInit } from '@angular/core';
import { Audiobook } from '../../model/audiobook';
import { AudiobooksService } from '../../services/audiobooks.service';

@Component({
  selector: 'app-library-tab',
  templateUrl: './library-tab.component.html',
  styleUrls: ['./library-tab.component.scss']
})
export class LibraryTabComponent implements OnInit {

  private audiobooks: Audiobook[];

  constructor(private audiobooksService: AudiobooksService) {}

  ngOnInit() {
    this.getAudiobooks();
    console.log(this.audiobooks);
  }

  getAudiobooks(): void {
    this.audiobooksService.getAudiobooks()
      .subscribe((audiobooks) => this.audiobooks = audiobooks);
  }
}
