# Docker-Fish
 Dockerized SocialFish with uwsgi & nginx


### USING GIT REPO

```sh
$ sudo git clone https://github.com/NOXCIS/Docker-Fish.git
$ cd Docker-Fish
```
# CHANGE DEFAULT LOGIN CREDS & SECRET KEY

```sh
$ sudo chmod +x ChangePassword.sh

$ sudo ./ChangePassword.sh

$ docker-compose up --build
```
#Login can be found on your_host_ip/neptune 

Deafult username: kali 

Deafult password: 1234





### USING DOCKER


Using image
```sh
$ sudo docker pull noxcis/docker-socialfish
$ sudo docker run --publish 80:80 noxcis/docker-socialfish
```
Login can be found on your_host_ip/neptune 

Deafult username: kali 
Deafult password: 1234






## DISCLAIMER

TO BE USED FOR EDUCATIONAL PURPOSES ONLY

The use of the SocialFish is COMPLETE RESPONSIBILITY of the END-USER. Developers assume NO liability and are NOT responsible for any misuse or damage caused by this program.

"DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE."
Taken from [LICENSE](LICENSE).
