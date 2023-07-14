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

// function downdateImage() {
//   const choiceImgElement1 = document.getElementById("choiceImg_01");
//   const choiceImgElement2 = document.getElementById("choiceImg_02");
//   const imagePath1 = `../img/choice1/choice_${count - 1}.png`;
//   const imagePath2 = `../img/choice2/choice_${count - 1}.png`;
//   choiceImgElement1.src = imagePath1;
//   choiceImgElement2.src = imagePath2;
//   count--;
// }

function downdateImage() {
  if (count >= 1) {
    count--;
    const choiceImgElement1 = document.getElementById("choiceImg_01");
    const choiceImgElement2 = document.getElementById("choiceImg_02");
    const imagePath1 = `../img/choice1/choice_${count}.png`;
    const imagePath2 = `../img/choice2/choice_${count}.png`;
    choiceImgElement1.src = imagePath1;
    choiceImgElement2.src = imagePath2;
  }
}
