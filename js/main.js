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
}

function downdateImage() {
  const choiceImgElement1 = document.getElementById("choiceImg_01");
  const choiceImgElement2 = document.getElementById("choiceImg_02");
  const imagePath1 = `../img/choice1/choice_${count - 1}.png`;
  const imagePath2 = `../img/choice2/choice_${count - 1}.png`;
  choiceImgElement1.src = imagePath1;
  choiceImgElement2.src = imagePath2;
  count--;
}

// // '이전으로' 버튼 클릭 시 이전 페이지로 이동
// const prevButton = document.querySelector(".prevButton");
// prevButton.addEventListener("click", function () {
//   const currentPageIndex = parseInt(
//     window.location.pathname.split("_")[1].split(".")[0]
//   );
//   const previousPageIndex = currentPageIndex - 1;
//   if (previousPageIndex >= 1) {
//     const previousPage = `choice_${previousPageIndex}.html`;
//     goToNextPage(previousPage);
//   }
// });

// // // 페이지 로드 시 이미지 업데이트
// // window.addEventListener("DOMContentLoaded", function () {
// //   const currentPageIndex = parseInt(
// //     window.location.pathname.split("_")[1].split(".")[0]
// //   );
// //   updateImage(currentPageIndex);
// // });
