"""
    정렬 : Sort : 데이터[자료]들을 일정한 순서대로 나열
        * 정렬된 데이터들은 검색 빠르다.
        * 오름차순[ASC] / 내림차순 [ DESC ]
        1. 선택정렬 [ Selection sort ]
            * 여러 데이터들 중에서 가장 작은 값/큰값 을 뽑는 과정을 반복하여 값 정렬 한다.
            * 최소값을 찾아서 순서대로 새로운곳에 배치
            172 180 163 153 190         ->  153
            172 180 163 190                ->  153 163
            172 180 190                       ->  153 163
            180 190                              ->  153 163 172
            190                                    ->  153 163 172 180
                                                      ->  153 163 172 180 190
            * 교환 정렬
                해당 인덱스 다른 인덱스 비교
            172 180 163 153 190         -> 172 > 180  false
            172 180 163 153 190         -> 172 > 163  true        163 180 172 153 190
            163 180 172 153 190         -> 163 > 153  true        153 180 172  163 190
            153 180 172  163 190        -> 153 > 190  false       153 180 172  163 190

        2. 삽입정렬 [ Insertion sort ]

        3. 버블정렬 [ Bubble sort ]
        4. 퀵정렬 [ Quick sort ]
"""