class thailandpackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 방콕, 파타야 여행 (야시장 투어) 50만원")

# 모듈을 직접실행
if __name__ == "__main__":
    print("thailand 모듈을 직접 실행")
    trip_to = thailandpackage()
    trip_to.detail()
else:
    print("thailand 외부에서 모듈호출")