import { TestBed, inject } from '@angular/core/testing';

import { AudiobooksService } from './audiobooks.service';

describe('AudiobooksService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [AudiobooksService]
    });
  });

  it('should be created', inject([AudiobooksService], (service: AudiobooksService) => {
    expect(service).toBeTruthy();
  }));
});
