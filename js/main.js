// // 페이지 이동 함수
function goToNextPage(page) {
  window.location.href = page;
}

// // 이미지 변경 함수
let count = 1;
function updateImage() {
  const choiceImgElement1 = document.getElementById("choiceImg_01");
  const choiceImgElement2 = document.getElementById("choiceImg_02");
  const imagePath1 = `../img/choice1/choice_${count}.png`; // 각 선택지에 해당하는 이미지 경로
  const imagePath2 = `../img/choice2/choice_${count}.png`; // 각 선택지에 해당하는 이미지 경로
  choiceImgElement1.src = imagePath1;
  choiceImgElement2.src = imagePath2;
  count++;

  if (count > 10) {
    openResultModal();
  }
}

function downdateImage() {
  if (count >= 1) {
    count--;
    const choiceImgElement1 = document.getElementById("choiceImg_01");
    const choiceImgElement2 = document.getElementById("choiceImg_02");
    const imagePath1 = `../img/choice1/choice_${count}.png`;
    const imagePath2 = `../img/choice2/choice_${count}.png`;
    choiceImgElement1.src = imagePath1;
    choiceImgElement2.src = imagePath2;

    if (count === 0) {
      openPreviousModal();
    }
  }
}

// 이전 모달 열기
function openPreviousModal() {
  const modal = document.getElementById("previousModal");
  modal.style.display = "block";

  // 닫기 버튼 클릭 시 모달 창 닫기
  const closeButton = document.querySelector("#previousModal .close");
  closeButton.onclick = function () {
    modal.style.display = "none";
  };
}

// 결과보기 모달 열기
function openResultModal() {
  const modal = document.getElementById("resultModal");
  modal.style.display = "block";

  // 결과보기 버튼 클릭 시 이벤트 핸들러 등록
  const resultButton = document.getElementById("resultButton");
  resultButton.addEventListener("click", function () {
    // 사용자의 성별과 나이대 정보 가져오기
    const gender = document.getElementById("gender").value;
    const age = document.getElementById("age").value;

    // 결과 페이지로 이동
    const resultPage = `./resultKind.html?gender=${gender}&age=${age}`;
    goToNextPage(resultPage);
  });

  // 닫기 버튼 클릭 시 모달 창 닫기
  const closeButton = document.querySelector("#resultModal .close");
  closeButton.onclick = function () {
    modal.style.display = "none";
  };
}

// 모달 창 닫기 버튼 클릭 시 이벤트 핸들러
const closeButton = document.querySelector(".modal .close");
closeButton.onclick = function () {
  const modal = this.closest(".modal");
  modal.style.display = "none";
};

// 페이지 로드 시 모달 창 열기
window.addEventListener("load", function () {
  const modal = document.getElementById("myModal");
  modal.style.display = "block";
});
