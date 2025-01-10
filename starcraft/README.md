## code review starcraft.cpp
### static int total_marine_num;
static 멤버 변수
- 모든 객체가 한 메모리를 공유하는 멤버 변수
- class 바깥에서 초기화
### Marine& be_attacked(int damage_earn);
레퍼런스를 리턴하는 함수
- 객체를 리턴하기 때문에
- marine2.be_attacked(marine1.attack()).be_attacked(marine1.attack());
- 처럼 함수를 여러번 호출할 수 있다
### ~Marine() { total_marine_num--; }
소멸자 static 멤버 변수 marine_num을 감소
